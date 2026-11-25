import { useAppStyles } from '@/styles/style';
import { View , Text} from "react-native";



export default function Nav() {
const { styles } = useAppStyles();
  return (
    <View style={styles.nav}>
    <Text style={styles.label}>Hello world</Text>
    </View>
  );
}