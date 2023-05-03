<template>
<div>
    <h2>결정새액 : {{finalTax()}}</h2>
</div>
</template>

<script>
export default {
    name: 'FinalTax',
    props: {
        afterTax: Number,
        taxCredit: Number,
    },
    methods : {
        finalTax() {
            return this.afterTax -this.taxCredit >=0? this.afterTax-this.taxCredit :0
        }
    },
}
</script>

<style>

</style>