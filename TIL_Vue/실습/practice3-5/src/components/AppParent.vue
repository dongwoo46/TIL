<template>
    <div>
        <h1>AppParent</h1>
        <input type="text" v-model='msg2'>
        <p>appData : {{appMsg}}</p>
        <p>childData : {{}}</p>
        <AppChild :appParentMsg='msg2' :appMsg='msg'/>
    </div>
</template>

<script>
import AppChild from './AppChild.vue'
export default {
    name: 'AppParent',
    props: {
        appMsg : Number,
        
    },
    components: {
        AppChild,
    },
    data: function() {
        return {
            msg2 : ''
        }
        
    }
}
</script>

<style>

</style>