<template>
  <div>
    <h1>AppParent</h1>
    <!-- parent input에 입력이 되면 해당 함수가 실행 -->
    <input type="text" v-model="parentData" @input="onParentInputChange">
    <p>appData: {{appData}}</p>
    <p>childData: {{childData}}</p>
    <!-- child로 appData와 parentData값 props하고 childData값 가지고 오기 -->
    <AppChild :app-data="appData" :parent-data="parentData" @child-input-change="onChildInputChange"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
    name:'AppParent',
    components: {
        AppChild,
    },
    // appData값 가져오기
    props: {
        appData:String,
    },
    data() {
        return {
            //필요한 data값 생성
            parentData:null,
            childData:null,
        }
    },
    methods: {
        // 왜 ParentInputChange의 변수는 event이고 ChildInputChange는 childInputData인가? => 현재 childData는 이전 AppChild에서 받아온 값 그대로 사용 한것이고 
        // parentData는 현재 AppParent에서 새로이 값을 설정해줘야하기 때문 즉 이전에 받아온 데이터값을 새로 보내는건 ~~InputData써도 되지만 
        // 새로이 데이터를 보내는 것이라면 event.target.value 사용이 필수

        // parent에 입력값의 변화가 생기면 parent-input-change함수 발동하고 현재 입력값을 부모로 보내기 
        onParentInputChange : function(event) {
            this.$emit('parent-input-change', event.target.value)
        },
        // child의 입력값의 변화 생기면 child-input-chage 함수 발동하고 현재 child의 입력값을 바꿔주고 부모로 보내기
        onChildInputChange : function(childInputData) {
            this.childData = childInputData
            this.$emit('child-input-change', childInputData)
        }
    }
}
</script>

<style>

</style>