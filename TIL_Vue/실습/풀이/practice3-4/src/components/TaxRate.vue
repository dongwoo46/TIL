<template>
  <div>
    <h2>산출 세액 : {{afterTax}} </h2>
    <h2>세액 감면 : (-) {{taxCredit}} 만원</h2>
    <hr>
    <FinalTax :afterTax='afterTax' :taxCredit="taxCredit"/>

  </div>
</template>

<script>
import FinalTax from './FinalTax.vue'
export default {
    name: 'TaxRate',
    props: {
        taxBase: Number,
        taxCredit: Number,
    },
    components: {
        FinalTax,
    },
    computed: {
        afterTax() {
            if (this.taxBase <= 1200) {
        return Math.round(this.taxBase * 0.06)
        } else if (this.taxBase > 1200 && this.taxBase <= 4600) {
        return Math.round(this.taxBase * 0.15 - 108)
        } else if (this.taxBase > 4600 && this.taxBase <= 8800) {
        return Math.round(this.taxBase * 0.24 - 522)
        } else if (this.taxBase > 8800 && this.taxBase <= 15000) {
        return Math.round(this.taxBase * 0.35 - 1490)
        } else if (this.taxBase > 15000 && this.taxBase <= 30000) {
        return Math.round(this.taxBase * 0.38 - 1940)
        } else if (this.taxBase > 30000 && this.taxBase <= 50000) {
        return Math.round(this.taxBase * 0.4 - 2540)
        } else if (this.taxBase > 50000 && this.taxBase <= 100000) {
        return Math.round(this.taxBase * 0.42 - 3540)
        } else {
        return Math.round(this.taxBase * 0.45 - 6540)
        }
        }
    }
        
}
</script>

<style>

</style>