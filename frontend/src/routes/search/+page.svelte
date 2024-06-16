<script lang="ts">
    import SearchResult from '$lib/SearchResult.svelte';
    import { containsSyriac } from '$lib/containsSyriac';
    import { transliterateToSyriac } from '$lib/transliterate';

    let query: string = "";
    let results: Promise<any[]> | null = null;

    $: handleQuery(query);

    function handleQuery(query: string) {
        query = transliterateToSyriac(query);
        results = query ? fetchResults(query) : null;
    }

    async function fetchResults(query: string): Promise<any[]> {
        try {
            const response = await fetch('https://mattynaz--assyrian-digital-library-webapp-web.modal.run/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Fetch error:', error);
            throw error;
        }
    }
</script>

<section class="flex flex-col gap-4 my-8">
    <div class="flex flex-row gap-2 border-b-2 bg-gray-50 focus-within:border-gray-300 p-2 rounded-sm">
        <span class="material-symbols-outlined select-none text-gray-400">
            search
        </span>
        <input placeholder="Search..." class="w-full bg-transparent outline-none placeholder:text-gray-400 {containsSyriac(query) ? "font-['Noto_Sans_Syriac_Eastern'] font-medium" : ""}" type="text" bind:value={query} />
    </div>

    {#if results}
        {#await results}
            <p class="text-sm border border-blue-500 bg-blue-50 px-2 py-1">
                <span class="animate-pulse">Searching...</span>
            </p>
        {:then resolvedResults}
            {#if resolvedResults.length == 0}
                <p class="text-sm border border-red-500 bg-red-50 px-2 py-1">
                    Found no results
                </p>
            {:else}
                <p class="text-sm border border-green-500 bg-green-50 px-2 py-1">
                    Found {resolvedResults.length} results
                </p>
            {/if}
        {:catch error}
            <p class="text-sm border border-red-500 bg-red-50 px-2 py-1">
                Error: {error.message}
            </p>
        {/await}
    {/if}
</section>


{#if results}
    {#await results then resolvedResults}
        <ol class="flex flex-col gap-6">
            {#each resolvedResults as result}
                <li>
                    <SearchResult {...result} />
                </li>
            {/each}
        </ol>
    {/await}
{/if}
