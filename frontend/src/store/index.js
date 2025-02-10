import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      // Define your state properties here
      isAuthenticated: false,
    };
  },
  mutations: {
    // Define your mutations here
    setAuthenticated(state, status) {
      state.isAuthenticated = status;
    }
  },
  actions: {
    // Define your actions here
    login({ commit }, token) {
      // Save token to local storage
      localStorage.setItem('authToken', token);
      commit('setAuthenticated', true);
    },
    logout({ commit }) {
      // Remove token from local storage
      localStorage.removeItem('authToken');
      commit('setAuthenticated', false);
    }
  },
  getters: {
    // Define your getters here
    isAuthenticated: (state) => state.isAuthenticated,
  }
});

export default store;
