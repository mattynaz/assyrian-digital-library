import glob
import os
import re
import difflib
from dataclasses import dataclass

@dataclass
class Text:
    title: str
    author: str
    date: str
    content: str

@dataclass
class SearchResult:
    title: str
    author: str
    date: str
    content: str
    span: tuple[int, int]
    location: int

def parse_filename(filename: str) -> tuple[str, str, str]:
    basename = os.path.basename(filename)
    name, _ = os.path.splitext(basename)
    parts = name.split('_')
    if len(parts) != 3:
        raise ValueError(f"Filename {filename} does not match the expected format 'title_Author_year.md'")
    title, author, date = parts
    return title, author, date

def parse_texts(folder_path: str) -> list[Text]:
    texts = []
    for filepath in glob.glob(os.path.join(folder_path, '*.md')):
        try:
            title, author, date = parse_filename(filepath)
            with open(filepath, 'r') as file:
                content = file.read()
            texts.append(Text(title, author, date, content))
        except ValueError as e:
            print(f"Skipping file {filepath}: {e}")
    return texts

def compile_search_query(query: str) -> re.Pattern:
    diacritics = "[◌̰݈̮ܸܼܹ݂̣̃݇ܲܵܿ̇̈]"
    bounaries = "[ ,.?!:;]"
    proclitics = (
        "ܕ",
        "ܠ",
        "ܒ",
        "ܘ",
    )
    enclitics = (
        "ܐ",
        "ܬܐ",
        "ܢܐ",
        "ܝܐ",
        "ܘܬܐ",
        "ܢ",
        "ܘܟ",
        "ܟ",
        "ܝ",
        "ܗ",
        "ܗܝ",
    )

    remove_diacritics = lambda s: re.sub(diacritics, "", s)
    pad_diacritics = lambda s: re.sub("(?<=.)", f"{diacritics}*", s)
    prepare_clitics = lambda clitics: "|".join(map(pad_diacritics, clitics))
    
    pattern = query.rstrip("ܐ")
    print(pattern)
    pattern = remove_diacritics(pattern)
    print(pattern)
    pattern = (
        f"{bounaries}"
        f"(?:{prepare_clitics(proclitics)})?"
        f"({pad_diacritics(pattern)}"
        f"(?:{prepare_clitics(enclitics)})?)"
        f"{bounaries}"
    )
    print(pattern)
    return re.compile(pattern, re.IGNORECASE)

def search_texts(query: str, texts: list[Text], preview_len: int = 60, max_results_per_text: int = 40) -> list[SearchResult]:
    results = []
    if not query:
        return results
    pattern = compile_search_query(query)
    for text in texts:
        matches_count = 0
        for match in pattern.finditer(text.content):
            if matches_count >= max_results_per_text:
                break
            
            # Extract a snippet of text around the match
            start = text.content.rfind(' ', 0, max(0, match.start(1) - preview_len)) + 1
            end = text.content.find(' ', match.end(1) + preview_len)
            if end == -1:
                end = len(text.content)
            content = text.content[start:end]
            
            # Add the search result to the list
            span = (match.start(1) - start, match.end(1) - start)
            results.append(SearchResult(text.title, text.author, text.date, content, span, start))
            matches_count += 1

    # Sort the results by levenstein distance of match to query
    levenshtein = lambda a, b: difflib.SequenceMatcher(None, a, b).ratio()
    results.sort(key=lambda r: levenshtein(query, r.content[r.span[0]:r.span[1]]), reverse=True)
    return results
