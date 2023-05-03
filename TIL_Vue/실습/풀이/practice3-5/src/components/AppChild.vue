<template>
<div>
    <h1>AppParent</h1>
    <!-- parent input에 입력이 되면 해당 함수가 실행 -->
    <input type="text" v-model="childData" @input="onChildInputChange">
    <p>appData: {{appData}}</p>
    <p>parentData : {{parentData}}</p>
    <p>childData: {{childData}}</p>
</div>
    
</template>

<script>
export default {
    name: 'AppChild',
    props: {
        appData:String,
        parentData: String,
    },
    data() {
        return {
            childData: null
        }
    },
    methods: {
        onChildInputChange: function(event) {
            this.$emit('child-input-change', event.target.value )
        }
    }
}
</script>

<style>

</style>