<script lang="ts">
    import "../app.css";
    import { page } from '$app/stores';

    function isActive(path: string): string {
        return $page.url.pathname === path ? 'text-blue-600' : '';
    };
</script>

<div class="w-full max-w-screen-md mx-auto p-4">
    <header class="flex flex-row items-center mb-8">
        <a href="/" class="contents">
            <hgroup class="flex flex-row items-center select-none">
                <span class="material-symbols-outlined text-7xl">
                    two_pager
                </span>
                <h1 class="font-extrabold flex flex-col leading-none">
                    <span>Assyrian</span>
                    <span class="text-blue-600">Digital</span>
                    <span>Library</span>
                </h1>
            </hgroup>
        </a>
        {#key $page.url.pathname}
            <ol class="flex gap-4 ml-auto text-sm font-medium">
                <li class={isActive('/')}>
                    <a href="/" class="hover:underline">Home</a>
                </li>
                <li class={isActive('/search')}>
                    <a href="/search" class="hover:underline">Search</a>
                </li>
                <li class={isActive('/about')}>
                    <a href="/about" class="hover:underline">About</a>
                </li>
            </ol>
        {/key}
    </header>
        
    <slot />
</div>