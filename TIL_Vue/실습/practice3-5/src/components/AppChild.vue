<template>
    <div>
        <h1>AppChild</h1>
        <input type="number" v-model.number='msg3'>
        <p>appData : {{appMsg}} </p>
        <p>parentData : {{appParentMsg}}</p>
        <p>childData : {{msg3}}</p>
    </div>
</template>

<script>
export default {
    name : "AppChild",
    props : {
        appParentMsg : Number,
        appMsg : Number,
    },
    data: function () {
        return {
            msg3 : '',
        }
    },
}
</script>

<style>

</style>