import { View, Text } from 'react-native';
import { useAppStyles } from "@/styles/style";

export  default function WorkoutPlanner() {
  const { styles } = useAppStyles();

  return (
    <View style={styles.screen}>
      <View style={styles.container}>
        <Text style={styles.title}>Workout Planner</Text>
      </View>
    </View>
  );
}