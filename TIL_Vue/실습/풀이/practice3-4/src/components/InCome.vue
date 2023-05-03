<template>
    <div>
        <div>
            <!-- 종합 소득금액 -->
            <label for="income">연봉 입력(만원) : </label>
            <input id="income" type="number" v-model.number="income">
        </div>
        <div>
            <!-- 종합 소득금액 -->
            <label for="tax-credit">세액 감면액(만원) : </label>
            <input id="tax-credit" type="number" v-model.number="taxCredit">
        </div>
        <br>
        <hr>
        
        <h2>종합 소득 금액: {{income}} 만원</h2>
        <h2>종합 소득 공제 : (-) 150 만원</h2>
        <h2>과세 표준 : {{taxBase}}</h2>
        <hr>
        <TaxRate :taxBase='taxBase' :taxCredit="taxCredit"/>
        

    </div>

</template>

<script>
import TaxRate from './TaxRate.vue'
export default {
    name: 'InCome',
    components: {
        TaxRate,
    },
    data: function() {
        return {
            income : 0,
            taxCredit : 0,
        }
    },
    computed: {
        taxBase() {
            return this.income - 150 >=0 ? this.income-150:0
        }
    }
}
</script>

<style>

</style>