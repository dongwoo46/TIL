import AllTodoPage from '@/components/AllTodoPage'
import TodayTodoPage from '@/components/TodayTodoPage'
import ImportantTodoPage from '@/components/ImportantTodoPage'

// 모듈 활용
const todo = {
  state: {
    todos: [
      {
        id: 1,
        content: 'Vue',
        dueDateTime: '2023-05-03T14:30',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 2,
        content: 'Vue Router',
        dueDateTime: '2023-05-10T14:30',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 3,
        content: 'Vuex',
        dueDateTime: '2023-05-08T14:30',
        isCompleted: true,
        isImportant: false,
      }
    ],
    selectedComponent: AllTodoPage,
    classStatus: {
      selectedAll: true,
      selectedToday: false,
      selectedImportant: false,
    }
  },
  getters: {
    currentComponent (state) {
      return state.selectedComponent
    },
    currentClassStatus (state) {
      return state.classStatus
    }
  },
  mutations: {
    // 보여줄 컴포넌트 변경
    CHANGE_COMPONENT (state, component) {
      if (component === 'all') {
        state.selectedComponent = AllTodoPage
      } else if (component === 'today') {
        state.selectedComponent = TodayTodoPage
      } else if (component === 'important') {
        state.selectedComponent = ImportantTodoPage
      }
    },
    // SideBar의 링크 글자색 변경
    CHANGE_CLASS_STATUS (state, select) {
      if (select === 'all') {
        state.classStatus.selectedAll = true
        state.classStatus.selectedToday = false
        state.classStatus.selectedImportant = false
      } else if (select === 'today') {
        state.classStatus.selectedAll = false
        state.classStatus.selectedToday = true
        state.classStatus.selectedImportant = false
      } else if (select === 'important') {
        state.classStatus.selectedAll = false
        state.classStatus.selectedToday = false
        state.classStatus.selectedImportant = true
      }
    }
  },
  actions: {
    changeComponent (context, component) {
      context.commit('CHANGE_COMPONENT', component)
    },

    changeClassStatus (context, select) {
      context.commit('CHANGE_CLASS_STATUS', select)
    }
  },
}

export default todo