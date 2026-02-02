#!/usr/bin/env ruby
# frozen_string_literal: true

def each_query_block(lines)
  i = 0
  while i < lines.length
    line = lines[i]
    if line.match?(/^\s*-\s*\[q\d+\]\s*\([^)]+\)\s+/)
      qline_no = i + 1
      qtext = line
      tool_lines = []

      j = i + 1
      while j < lines.length
        break if lines[j].match?(/^\s*-\s*\[q\d+\]\s*\([^)]+\)\s+/)
        break if lines[j].match?(/^##\s+topics\//)
        tool_lines << [j + 1, lines[j]] if lines[j].match?(/^\s*-\s*tool:\s*`[^`]+`\s*$/)
        j += 1
      end

      yield(qline_no, qtext, tool_lines)
      i = j
      next
    end
    i += 1
  end
end

def tool_value(line)
  line[/^\s*-\s*tool:\s*`([^`]+)`\s*$/, 1]
end

def stable_tool_id?(v)
  return true if v.start_with?('toolshed.g2.bx.psu.edu/')
  return true if v.start_with?('interactive_tool_')
  return true if v == 'upload1'
  return true if v.match?(/^__\w+__$/)
  false
end

def check_file(path)
  lines = File.read(path, encoding: 'UTF-8').lines
  problems = 0

  each_query_block(lines) do |qline_no, qtext, tool_lines|
    unless tool_lines.size == 1
      problems += 1
      warn "#{path}:#{qline_no}: query has #{tool_lines.size} tool lines (expected 1)"
    end

    q = qtext.strip

    problems += 1 && warn("#{path}:#{qline_no}: query mentions 'tutorial'") if q.match?(/\btutorial\b/i)
    problems += 1 && warn("#{path}:#{qline_no}: query looks like configuration help, not tool recommendation") if q.match?(/\b(configure|configuration|parameters?|set (the )?options|which inputs|select and how)\b/i)
    problems += 1 && warn("#{path}:#{qline_no}: query still contains Inputs:/Requirements:") if q.include?('Inputs:') || q.include?('Requirements:')

    if q.match?(/`[^`]*\.(fastq|fq|fasta|fa|bam|sam|vcf|bed|gtf|gff|tsv|csv|txt|json|yaml|yml|h5ad|loom|mzml|mgf|zip|tar|gz)(\.[^`]*)?`/i)
      problems += 1
      warn "#{path}:#{qline_no}: query contains a file-like token"
    end

    if q.match?(/`(?:SRR|ERR|DRR)\d+[^`]*`/i) || q.match?(/`E-MTAB-\d+`/i) || q.match?(/`GSE\d+`/i) || q.match?(/`GSM\d+`/i)
      problems += 1
      warn "#{path}:#{qline_no}: query contains an accession-like token"
    end

    tool_lines.each do |tline_no, tline|
      v = tool_value(tline)
      next unless v

      unless stable_tool_id?(v)
        if v.match?(/^[A-Za-z0-9_]+$/)
          warn "#{path}:#{tline_no}: WARN: tool id is non-toolshed/internal-looking: #{v}"
        else
          problems += 1
          warn "#{path}:#{tline_no}: tool id is not stable (should be Toolshed GUID or allowed special id): #{v}"
        end
      end
    end
  end

  problems
end

if ARGV.empty?
  warn "usage: #{File.basename($PROGRAM_NAME)} <md files...>"
  exit 2
end

total = 0
ARGV.each do |path|
  next unless File.exist?(path)
  total += check_file(path)
end

exit(total.zero? ? 0 : 1)

