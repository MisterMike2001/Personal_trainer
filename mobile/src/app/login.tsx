import { useState } from 'react';
import { Alert, View, Text, Button, TextInput } from 'react-native';

import { useAppStyles } from '@/styles/style';
import { useAuth } from '@/context/auth_context';

export default function LoginScreen() {
  const { styles, colors } = useAppStyles();
  const { signIn } = useAuth();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleLogin = async () => {
    if (isSubmitting) return;

    if (!email.trim() || !password) {
      Alert.alert('Missing details', 'Enter your email and password.');
      return;
    }

    setIsSubmitting(true);

    try {
      await signIn(email.trim(), password);
      // Your auth layout automatically opens the tabs.
    } catch {
      Alert.alert(
        'Login failed',
        'Check your credentials and connection, then try again.',
      );
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
  <View style={styles.screen}>
    <View style={[styles.container, { flex: 1, justifyContent: 'center' }]}>
      <View style={styles.card}>
        <Text style={styles.heading}>Welcome - Please Login</Text>

          <Text style={styles.label}>Email</Text>
          <TextInput
            style={styles.input}
            placeholder="Enter your email"
            placeholderTextColor={colors.muted}
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
            autoCorrect={false}
            autoComplete="email"
            editable={!isSubmitting}
          />

          <Text style={styles.label}>Password</Text>
          <TextInput
            style={styles.input}
            placeholder="Enter your password"
            placeholderTextColor={colors.muted}
            value={password}
            onChangeText={setPassword}
            secureTextEntry
            autoCapitalize="none"
            autoCorrect={false}
            autoComplete="current-password"
            editable={!isSubmitting}
          />

          <Button
            title={isSubmitting ? 'Signing in…' : 'Login'}
            onPress={handleLogin}
            disabled={isSubmitting}
          />
        </View>
      </View>
    </View>
  );
}