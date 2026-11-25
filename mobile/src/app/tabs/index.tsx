import { View, Text } from 'react-native';

import { useAppStyles } from '@/styles/style';

export default function HomeScreen() {
  const { styles } = useAppStyles();

  return (
    <View style={styles.screen}>
      <View style={styles.container}>
        <Text style={styles.title}>Personal Trainer</Text>
      </View>
    </View>
  );
}