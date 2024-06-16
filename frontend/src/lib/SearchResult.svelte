<script lang="ts">
    export let title: string
    export let author: string
    export let date: string
    export let content: string
    export let span: number[]
    export let location: number
</script>

<div>
    <p class="w-full text-ellipsis text-nowrap overflow-hidden font-['Noto_Sans_Syriac_Eastern'] font-semibold">
        {content.slice(0, span[0])}
        <span class="bg-yellow-300">
            {content.slice(span[0], span[1])}
        </span>
        {content.slice(span[1])}
    </p>
    <p class="text-sm text-gray-400">
        {author} <i>{title}</i> ({date}) (loc. {location})
    </p>
</div>
