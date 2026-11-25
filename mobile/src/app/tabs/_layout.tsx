import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

import { useAppStyles } from '@/styles/style';

export default function RootLayout() {
  const { colors } = useAppStyles();

  return (
    <Tabs
      screenOptions={{
        headerStyle: {
          backgroundColor: colors.surface,
        },
        headerTintColor: colors.text,
        sceneStyle: {
          backgroundColor: colors.background,
        },
        tabBarStyle: {
          backgroundColor: colors.surface,
          borderTopColor: colors.border,
        },
        tabBarActiveTintColor: colors.primary,
        tabBarInactiveTintColor: colors.muted,
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="home-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />

      <Tabs.Screen
        name="workout_planner"
        options={{
          title: 'Planner',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="calendar-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />
        <Tabs.Screen
        name="workout_tracker"
        options={{
          title: 'Tracker',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="fitness-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />
      <Tabs.Screen
        name="progress_tracker"
        options={{
          title: 'Progress',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="bar-chart-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />
      <Tabs.Screen
        name="profile_management"
        options={{
          title: 'Profile',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="person-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />
      <Tabs.Screen
        name="logout"
        options={{
          title: 'Logout',
          tabBarIcon: ({ focused, size }) => (
            <Ionicons name="log-out-outline" size={size} color={focused ? colors.primary : colors.muted} />
          ),
          headerShown: false,
        }}
      />
    </Tabs>
  );
}
