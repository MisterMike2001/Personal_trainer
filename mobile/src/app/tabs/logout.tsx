import { View, Text, Pressable, ActivityIndicator, Alert } from 'react-native';
import { useAuth } from '@/context/auth_context';
import { useState } from 'react';
import { useAppStyles } from '@/styles/style';

export default function Logout() {
  const { signOut } = useAuth();
  const [isSubmitting, setIsSubmitting] = useState(false);
    const { styles, colors } = useAppStyles();
  async function handleLogout() {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      await signOut();
    } catch {
      Alert.alert('Logout failed', 'Check your connection and try again.');
    } finally {
      setIsSubmitting(false);
    }
  }

return (
  <View style={styles.screen}>
    <View style={[styles.container, { flex: 1, justifyContent: 'center' }]}>
      <View style={styles.card}>
        <Text style={styles.heading}>Log out?</Text>

        <Text style={[styles.body, styles.muted]}>
          You’ll need to sign in again to access your account.
        </Text>

        <Pressable
          accessibilityRole="button"
          accessibilityLabel="Log out"
          accessibilityState={{
            disabled: isSubmitting,
            busy: isSubmitting,
          }}
          onPress={handleLogout}
          disabled={isSubmitting}
          style={({ pressed }) => [
            styles.button,
            styles.buttonPrimary,
            isSubmitting && styles.buttonDisabled,
            pressed && styles.pressed,
          ]}
        >
          {isSubmitting ? (
            <ActivityIndicator color={colors.onDisabled} />
          ) : (
            <Text style={styles.buttonText}>Log out</Text>
          )}
        </Pressable>
      </View>
    </View>
  </View>
);
}
