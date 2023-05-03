<template>
    <div>
        <h1>check</h1>
        <p>
            <!-- 종합 소득금액 -->
            연봉 입력 (만원): <input type="number" v-model.number="revenue">
        </p>
        <p>
            <!-- 세액 감면액 -->
            세액감면액 (만원) : <input type="number" v-model.number="taxDiscount">
        </p>
        <hr>
        <div>
            <h2>종합 소득 금액 : {{revenue}} 만원</h2>
            <h2>종합 소득 공제 : {{deduction}}</h2>
            <h2>과세 표준 : {{revenue-deduction}} </h2>
            <TaxRate :my-props="dynamicProps"/>
        </div>
        <hr>

    </div>

</template>

<script>
export default {
    name: 'InCome',
    data: function() {
        return {
            revenue : 0,
            deduction : 150,
            dynamicProps: `${this.revenue}-${this.deduction}`
        }
    },
}
</script>

<style>

</style>