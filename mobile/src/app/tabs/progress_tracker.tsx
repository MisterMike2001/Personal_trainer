import { useAppStyles } from "@/styles/style";
import { View , Text} from "react-native";


export default function ProgressTracker() {
  const { styles } = useAppStyles();

  return (
    <View style={styles.screen}>
      <View style={styles.container}>
        <Text style={styles.title}>Progress Tracker</Text>
      </View>
    </View>
  );
}