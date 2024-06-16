// Function to check if a string contains any Syriac Unicode characters
export function containsSyriac(text: string): boolean {
    // Regular expression to match any Syriac Unicode character
    const syriacRegex = /[\u0700-\u074F]/;
    return syriacRegex.test(text);
}
