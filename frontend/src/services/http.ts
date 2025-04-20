import axios from 'axios';
import type { AxiosRequestConfig, AxiosResponse } from 'axios';

type ServiceParams = {
	json?: object;
	multipart?: FormData;
};

type RequestParams = { method: string } & ServiceParams;

class HTTPClient {
	private async send<T>(
		url: URL,
		{ method, json, multipart }: RequestParams
	): Promise<AxiosResponse<T, unknown>> {
		if (json && multipart) {
			throw 'cannot send both JSON and multipart data';
		}
		const options: AxiosRequestConfig = {
			method,
			headers: {},
			withCredentials: true
		};

		if (json) {
			options.headers = { 'Content-Type': 'application/json' };
			options.data = json;
		}
		if (multipart) {
			options.headers = { 'Content-Type': 'multipart/form-data' };
			options.data = multipart;
		}
		return await axios(url.toString(), options);
	}

	async get<T>(url: URL): Promise<AxiosResponse<T, unknown>> {
		return await this.send<T>(url, { method: 'GET' });
	}

	async post<T>(
		url: URL,
		{ json, multipart }: ServiceParams = {}
	): Promise<AxiosResponse<T, unknown>> {
		return await this.send(url, { method: 'POST', json, multipart });
	}

	async put<T>(
		url: URL,
		{ json, multipart }: ServiceParams = {}
	): Promise<AxiosResponse<T, unknown>> {
		return await this.send(url, { method: 'PUT', json, multipart });
	}

	async patch<T>(
		url: URL,
		{ json, multipart }: ServiceParams = {}
	): Promise<AxiosResponse<T, unknown>> {
		return await this.send(url, { method: 'PATCH', json, multipart });
	}

	async del<T>(url: URL): Promise<AxiosResponse<T, unknown>> {
		return await this.send(url, { method: 'DELETE' });
	}
}

// export singleton instance
export const client = new HTTPClient();
