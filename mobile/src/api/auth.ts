import axiosClient from "./axios_client";
import axios from 'axios';
import {saveTokens, getRefreshToken, clearTokens } from '@/services/tokens';

type TokenResponse ={
    access_token: string;
    refresh_token: string;
    token_type: string;
    expires_in: number;
}

export async function login(email: string, password: string): Promise<void> {
    try {
        const response = await axiosClient.post<TokenResponse>("/auth/login", { email, password });
        const { access_token, refresh_token } = response.data;
        await saveTokens(access_token, refresh_token);
    } catch (error) {
        console.error("Login failed:", error);
        throw error;
    }

}




export async function logout(): Promise<void> {
  const refreshToken = await getRefreshToken();

  if (refreshToken) {
    await axiosClient.post('/auth/logout', {
      refresh_token: refreshToken,
    });
  }

  await clearTokens();
}

export async function restoreSession(): Promise<boolean> {
  const refreshToken = await getRefreshToken();

  if (!refreshToken) {
    return false;
  }

  try {
    const response = await axiosClient.post<TokenResponse>(
      '/auth/refresh',
      { refresh_token: refreshToken },
    );

    await saveTokens(
      response.data.access_token,
      response.data.refresh_token,
    );

    return true;
  } catch (error) {
    if (
      axios.isAxiosError(error) &&
      error.response?.status === 401
    ) {
      await clearTokens();
      return false;
    }

    // Network errors shouldn't delete the user's session.
    throw error;
  }
}
