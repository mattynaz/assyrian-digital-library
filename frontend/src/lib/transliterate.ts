// Define the mapping for English to Syriac transliteration
const transliterationMap: { [key: string]: string } = {
    'ee': 'i',
    'oo': 'u',
    'ou': 'u',
    'gh': 'ܩ',
    'kh': 'ܚ',
    'sh': 'ܫ',
    'ch': 'ܟ̰',
    '\\b(a)': 'ܐܵ',
    '(a)\\b': 'ܵܐ',
    'a': 'ܵ',
    'b': 'ܒ',
    'c': 'ܟ',
    'd': 'ܕ',
    '\\b(e)': 'ܐܹ',
    '(e)\\b': 'ܹܐ',
    'e': 'ܹ',
    'f': 'ܖ',
    'g': 'ܓ',
    'h': 'ܗ',
    'i': 'ܝ̣',
    'j': 'ܓ̰',
    'k': 'ܟ',
    'l': 'ܠ',
    'm': 'ܡ',
    'n': 'ܢ',
    'o': 'ܘ̇',
    'p': 'ܦ',
    'q': 'ܩ',
    'r': 'ܪ',
    's': 'ܣ',
    't': 'ܬ',
    'u': 'ܘ̣',
    'v': 'ܘ',
    'w': 'ܘ',
    'x': 'ܚ',
    'y': 'ܝ',
    'z': 'ܙ',
};

// Function to transliterate English text into Syriac
export function transliterateToSyriac(text: string): string {
    text = text.toLowerCase();
    for (const [pattern, replacement] of Object.entries(transliterationMap)) {
        const regex = new RegExp(pattern, 'gi');
        text = text.replace(regex, replacement);
    }
    return text;
}
