//Compositional way to setup
/*
export const useAuthStore = defineStore("authStore", () => {
  //initial state
  const { email, token } =
    //access local storage only on client-side rendering
    process.client && JSON.parse(localStorage.getItem("authInfo") || "{}");
  const authInfo = ref({ email, token });

  //actions
  const setAuthInfo = (email: string, token: string) => {
    authInfo.value = { email, token };
    localStorage.setItem("authInfo", JSON.stringify(authInfo.value));
  };

  const clearAuthInfo = () => {
    authInfo.value = { email: null, token: null };
    localStorage.removeItem("authInfo");
  };

  return { authInfo, setAuthInfo, clearAuthInfo };

});
*/

//optional way,more common,easy to use plugins
export const useAuthStore = defineStore("authStore", {
  state: () => ({
    authInfo: {
      email: "",
      token: "",
    },
  }),
  actions: {
    setAuthInfo(email: string, token: string) {
      this.authInfo = { email, token };
    },
    clearAuthInfo() {
      this.authInfo = { email: "", token: "" };
    },
  },
  //Pinia-Plugin-Persistedstate (persisted in cookies by default)
  persist: true,
});
