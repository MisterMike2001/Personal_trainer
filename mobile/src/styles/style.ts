import { StyleSheet, useColorScheme } from 'react-native';

const themes = {
  light: {
    background: '#f8fafc',
    surface: '#ffffff',
    text: '#0f172a',
    muted: '#475569',
    primary: '#1d4ed8',
    onPrimary: '#ffffff',
    border: '#cbd5e1',
    danger: '#b91c1c',
    success: '#15803d',
    disabled: '#e2e8f0',
    onDisabled: '#64748b',
  },
  dark: {
    background: '#0f172a',
    surface: '#1e293b',
    text: '#f8fafc',
    muted: '#cbd5e1',
    primary: '#93c5fd',
    onPrimary: '#0f172a',
    border: '#475569',
    danger: '#fca5a5',
    success: '#86efac',
    disabled: '#334155',
    onDisabled: '#94a3b8',
  },
};

function createStyles(colors: typeof themes.light) {
  return StyleSheet.create({
    // Layout
    screen: {
      flex: 1,
      backgroundColor: colors.background,
    },
    container: {
      padding: 20,
      gap: 16,
    },
    row: {
      flexDirection: 'row',
      alignItems: 'center',
      gap: 12,
    },
    spaceBetween: {
      justifyContent: 'space-between',
    },
    center: {
      justifyContent: 'center',
      alignItems: 'center',
    },

    // Text
    title: {
      fontSize: 28,
      fontWeight: '700',
      marginTop: 25,
      color: colors.text,
    },
    heading: {
      fontSize: 20,
      fontWeight: '600',
      color: colors.text,
    },
    body: {
      fontSize: 16,
      lineHeight: 24,
      color: colors.text,
    },
    label: {
      fontSize: 14,
      fontWeight: '600',
      color: colors.text,
    },
    caption: {
      fontSize: 12,
      lineHeight: 18,
      color: colors.muted,
    },
    muted: {
      color: colors.muted,
    },
    error: {
      color: colors.danger,
    },
    success: {
      color: colors.success,
    },
    link: {
      color: colors.primary,
      textDecorationLine: 'underline',
    },

    // Buttons: combine button with a variant
    button: {
      minHeight: 48,
      paddingHorizontal: 20,
      paddingVertical: 12,
      borderRadius: 12,
      alignItems: 'center',
      justifyContent: 'center',
    },
    buttonPrimary: {
      backgroundColor: colors.primary,
    },
    buttonOutline: {
      borderWidth: 1,
      borderColor: colors.primary,
      backgroundColor: 'transparent',
    },
    buttonDisabled: {
      backgroundColor: colors.disabled,
      borderWidth: 0,
    },
    buttonText: {
      fontSize: 16,
      fontWeight: '600',
      color: colors.onPrimary,
    },
    buttonOutlineText: {
      color: colors.primary,
    },
    buttonDisabledText: {
      color: colors.onDisabled,
    },
    pressed: {
      opacity: 0.75,
    },

    // Forms
    field: {
      gap: 8,
    },
    input: {
      minHeight: 48,
      borderWidth: 1,
      borderColor: colors.border,
      borderRadius: 12,
      paddingHorizontal: 14,
      paddingVertical: 12,
      fontSize: 16,
      color: colors.text,
      backgroundColor: colors.surface,
    },
    inputFocused: {
      borderColor: colors.primary,
    },
    inputError: {
      borderColor: colors.danger,
    },

    // Cards and separators
    card: {
      backgroundColor: colors.surface,
      borderRadius: 16,
      borderWidth: 1,
      borderColor: colors.border,
      padding: 20,
      gap: 12,
    },
    divider: {
      height: 1,
      backgroundColor: colors.border,
    },

    // Navigation
    nav: {
      flexDirection: 'row',
      justifyContent: 'space-around',
      alignItems: 'center',
      backgroundColor: colors.surface,
      borderTopWidth: 1,
      borderTopColor: colors.border,
      paddingVertical: 12,
    },
    navItem: {
      minHeight: 48,
      paddingHorizontal: 16,
      alignItems: 'center',
      justifyContent: 'center',
    },
    navLabel: {
      fontSize: 14,
      fontWeight: '600',
      color: colors.muted,
    },
    navLabelActive: {
      color: colors.primary,
    },
  });
}

// Create both stylesheets once.
const lightStyles = createStyles(themes.light);
const darkStyles = createStyles(themes.dark);

// Call inside a component to follow the device's theme.
export function useAppStyles() {
  const isDark = useColorScheme() === 'dark';

  return {
    styles: isDark ? darkStyles : lightStyles,
    colors: isDark ? themes.dark : themes.light,
  };
}