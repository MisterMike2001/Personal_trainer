import * as SecureStore from 'expo-secure-store';

const REFRESH_TOKEN_KEY = 'refresh_token';

let accessToken: string | null = null;

export async function saveTokens(
    newAccessToken: string,
    newRefreshToken: string
) {
    accessToken = newAccessToken;
    await SecureStore.setItemAsync(REFRESH_TOKEN_KEY, newRefreshToken);
}

export function getAccessToken() {
    return accessToken;
}   

export async function getRefreshToken() {
    return await SecureStore.getItemAsync(REFRESH_TOKEN_KEY);
}

export async function clearTokens() {
    accessToken = null;
    await SecureStore.deleteItemAsync(REFRESH_TOKEN_KEY);
}