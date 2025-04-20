import type { ZodTypeAny } from 'zod';

import { client } from './http';

declare type ParamType = string | number | boolean | null;

export class BaseService<
	CreateType extends object | undefined,
	ReadType,
	UpdateType extends object | undefined
> {
	client = client;
	pathPrefix: string = '';
	readSchema!: ZodTypeAny;
	createSchema!: ZodTypeAny;
	updateSchema!: ZodTypeAny;

	buildUrl(path: string, params: Record<string, ParamType | Array<ParamType>> | null = null): URL {
		const url = new URL(`${import.meta.env.VITE_API_URL}${path}`);

		function addUrlParam(url: URL, key: string, value: ParamType): void {
			if (value === undefined) {
				throw new Error(`Value for key ${key} is undefined`);
			} else if (value === null) {
				return;
			}
			url.searchParams.append(key, value.toString());
		}
		if (params) {
			Object.keys(params).forEach((key) => {
				const value = params[key];
				if (Array.isArray(value)) {
					value.forEach((v) => addUrlParam(url, key, v));
				} else {
					addUrlParam(url, key, value);
				}
			});
		}
		return url;
	}

	async get(id: string): Promise<ReadType> {
		this.ensureArgs({ id });
		const url = this.buildUrl(`${this.pathPrefix}/${id}`);
		const response = await this.client.get(url);
		return this.readSchema.parse(response.data);
	}

	async add(data: CreateType): Promise<ReadType> {
		this.ensureArgs({data});
		const url = this.buildUrl(this.pathPrefix);
		const response = await this.client.post(url, { json: data });
		return this.readSchema.parse(response.data);
	}

	async update(id: string, data: UpdateType): Promise<ReadType> {
		this.ensureArgs({ id, data });
		const url = this.buildUrl(`${this.pathPrefix}/${id}`);
		const response = await this.client.put(url, { json: data });
		return this.readSchema.parse(response.data);
	}

	protected ensureArgs(args: Record<string, unknown>): void {
		Object.keys(args).forEach((key) => {
			if (args[key] === undefined) {
				throw new Error(`Argument ${key} is required`);
			}
		});
	}
}
