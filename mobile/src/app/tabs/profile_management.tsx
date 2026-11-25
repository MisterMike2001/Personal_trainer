import { useAppStyles } from "@/styles/style";
import { View , Text} from "react-native";



export default function ProfileManagement() {
    const { styles } = useAppStyles();

    return (
        <View style={styles.screen}>
            <View style={styles.container}>
                <Text style={styles.title}>Profile Management</Text>
            </View>
        </View>
    );
}   