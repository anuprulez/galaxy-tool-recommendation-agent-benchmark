#!/usr/bin/env ruby
# frozen_string_literal: true

require 'json'
require 'set'

ALLOWED_SPECIAL_TOOL_IDS = [
  'upload1'
].freeze

def stable_tool_id?(v)
  return true if v.start_with?('toolshed.g2.bx.psu.edu/')
  return true if v.start_with?('interactive_tool_')
  return true if ALLOWED_SPECIAL_TOOL_IDS.include?(v)
  return true if v.match?(/^__\w+__$/)
  # Galaxy core tool ids (e.g., Cut1, Filter1, Grep1) are stable enough for this benchmark,
  # but should be treated as a warning rather than an error by the caller.
  return true if v.match?(/^[A-Za-z0-9_]+$/)
  false
end

def tutorial_ids_from_yaml(path)
  ids = []
  File.foreach(path, encoding: 'UTF-8') do |line|
    m = line.match(/^\s*-\s*id:\s*(topics\/\S+)\s*$/)
    ids << m[1] if m
  end
  ids.uniq
end

def check_item(path, line_no, obj, tutorial_ids_set, ids_seen)
  problems = 0

  id = obj['id']
  tutorial_id = obj['tutorial_id']
  query = obj['query']
  tools = obj['tools']

  if !id.is_a?(String) || id.strip.empty?
    problems += 1
    warn "#{path}:#{line_no}: missing/invalid id"
  elsif ids_seen.include?(id)
    problems += 1
    warn "#{path}:#{line_no}: duplicate id: #{id}"
  else
    ids_seen.add(id)
  end

  if !tutorial_id.is_a?(String) || tutorial_id.strip.empty?
    problems += 1
    warn "#{path}:#{line_no}: missing/invalid tutorial_id"
  elsif !tutorial_ids_set.include?(tutorial_id)
    problems += 1
    warn "#{path}:#{line_no}: tutorial_id not in tutorial list: #{tutorial_id}"
  end

  if !query.is_a?(String) || query.strip.empty?
    problems += 1
    warn "#{path}:#{line_no}: missing/invalid query"
  else
    q = query
    if q.match?(/\btutorial\b/i) || q.match?(/\bGTN\b/i)
      problems += 1
      warn "#{path}:#{line_no}: query mentions tutorial/GTN"
    end

    if q.match?(/\b(configure|configuration|parameters?|set (the )?options|which inputs|select and how)\b/i)
      problems += 1
      warn "#{path}:#{line_no}: query looks like configuration help"
    end

    if q.match?(/https?:\/\//i)
      problems += 1
      warn "#{path}:#{line_no}: query contains a URL"
    end

    if q.match?(/\b(SRR|ERR|DRR)\d+\b/i) || q.match?(/\bE-MTAB-\d+\b/i) || q.match?(/\bGSE\d+\b/i) || q.match?(/\bGSM\d+\b/i)
      problems += 1
      warn "#{path}:#{line_no}: query contains an accession-like token"
    end

    if q.match?(/\.(fastq|fq|fasta|fa|bam|sam|vcf|bed|gtf|gff|tsv|csv|txt|json|yaml|yml|h5ad|loom|mzml|mgf|zip|tar|gz)\b/i)
      problems += 1
      warn "#{path}:#{line_no}: query contains a file-like extension"
    end
  end

  if !tools.is_a?(Array) || tools.empty? || !tools.all? { |t| t.is_a?(String) }
    problems += 1
    warn "#{path}:#{line_no}: missing/invalid tools array"
  else
    if tools.size != 1
      problems += 1
      warn "#{path}:#{line_no}: tools array size is #{tools.size} (expected 1)"
    end

    tools.each do |t|
      unless stable_tool_id?(t)
        problems += 1
        warn "#{path}:#{line_no}: non-stable tool id: #{t}"
      end
      if t.match?(/^[A-Za-z0-9_]+$/) && !t.start_with?('toolshed.g2.bx.psu.edu/') && !t.start_with?('interactive_tool_') && !t.match?(/^__\w+__$/) && !ALLOWED_SPECIAL_TOOL_IDS.include?(t)
        warn "#{path}:#{line_no}: WARN: tool id is Galaxy-internal/core-looking: #{t}"
      end
    end
  end

  problems
end

if ARGV.length != 1
  warn "usage: #{File.basename($PROGRAM_NAME)} data/benchmark/v1_items.jsonl"
  exit 2
end

path = ARGV[0]
unless File.exist?(path)
  warn "missing file: #{path}"
  exit 2
end

tutorial_list_path = 'data/tutorial_list_all_tools.yaml'
unless File.exist?(tutorial_list_path)
  warn "missing tutorial list: #{tutorial_list_path}"
  exit 2
end

tutorial_ids = tutorial_ids_from_yaml(tutorial_list_path)
tutorial_ids_set = tutorial_ids.to_h { |x| [x, true] }

ids_seen = Set.new

total = 0
File.foreach(path, encoding: 'UTF-8').with_index(1) do |line, line_no|
  next if line.strip.empty?
  begin
    obj = JSON.parse(line)
  rescue JSON::ParserError => e
    total += 1
    warn "#{path}:#{line_no}: invalid JSON: #{e.message}"
    next
  end
  total += check_item(path, line_no, obj, tutorial_ids_set, ids_seen)
end

exit(total.zero? ? 0 : 1)
