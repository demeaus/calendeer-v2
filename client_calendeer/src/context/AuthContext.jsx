import { createContext, useContext } from "react";

/**
 * Context makes user information global
 */

// TODO: Allow users to authenticate
const TEMP_USER = {
  id: 1,
  email: "deerdra@g.com",
};

const AuthContext = createContext();

function AuthProvider({ children }) {
  const user = TEMP_USER;

  return (
    <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>
  );
}

function useAuth() {
  const context = useContext(AuthContext);

  if (context === undefined) {
    throw new Error("AuthContext used outside of AuthProvider.");
  }
  return context;
}

export { AuthProvider, useAuth };
