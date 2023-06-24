//Compositional way to setup
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
