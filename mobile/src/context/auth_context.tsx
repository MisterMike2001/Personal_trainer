import {
  createContext,
  useContext,
  useEffect,
  useState,
  type PropsWithChildren,
} from 'react';

import { login, logout, restoreSession } from '@/api/auth';

type AuthContextValue = {
  isSignedIn: boolean;
  isLoading: boolean;
  error: string | null;
  retry: () => Promise<void>;
  signIn: (email: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | undefined>(
  undefined,
);

// Share startup restoration if effects run twice in development.
let restoration: Promise<boolean> | null = null;

function restoreOnce() {
  if (!restoration) {
    restoration = restoreSession().catch((error) => {
      restoration = null;
      throw error;
    });
  }

  return restoration;
}

export function AuthProvider({ children }: PropsWithChildren) {
  const [isSignedIn, setIsSignedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function checkSession() {
    setIsLoading(true);
    setError(null);

    try {
      setIsSignedIn(await restoreOnce());
    } catch {
      setError('Unable to connect. Check your connection and retry.');
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    void checkSession();
  }, []);

  async function signIn(email: string, password: string) {
    await login(email, password);

    restoration = Promise.resolve(true);
    setIsSignedIn(true);
  }

  async function signOut() {
    await logout();

    restoration = Promise.resolve(false);
    setIsSignedIn(false);
    setError(null);
  }

  return (
    <AuthContext.Provider
      value={{
        isSignedIn,
        isLoading,
        error,
        retry: checkSession,
        signIn,
        signOut,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth must be used inside AuthProvider');
  }

  return context;
}
