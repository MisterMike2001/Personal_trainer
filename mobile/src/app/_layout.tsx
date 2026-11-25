import { Stack } from 'expo-router';
import {
  ActivityIndicator,
  Button,
  Text,
  View,
} from 'react-native';

import {
  AuthProvider,
  useAuth,
} from '@/context/auth_context';

function Navigation() {
  const { isSignedIn, isLoading, error, retry } = useAuth();

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center' }}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', padding: 24 }}>
        <Text>{error}</Text>
        <Button title="Retry" onPress={() => void retry()} />
      </View>
    );
  }

  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Protected guard={isSignedIn}>
        <Stack.Screen name="tabs" />
      </Stack.Protected>

      <Stack.Protected guard={!isSignedIn}>
        <Stack.Screen name="login" />
      </Stack.Protected>
    </Stack>
  );
}

export default function RootLayout() {
  return (
    <AuthProvider>
      <Navigation />
    </AuthProvider>
  );
}