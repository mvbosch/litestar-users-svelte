import { BaseService } from '$lib/base_service';
import type { UserReadType, UserWriteType, AuthenticationSchemaType } from './schemas';
import { userReadSchema, userWriteSchema, authenticationSchema } from './schemas';

export class UserService extends BaseService<UserWriteType, UserReadType, UserWriteType> {
	pathPrefix: string = '/users';
	readSchema = userReadSchema;
	createSchema = userWriteSchema;

	async authenticate(data: AuthenticationSchemaType): Promise<UserReadType> {
		this.ensureArgs({ data });
		const url = this.buildUrl('/login');
		const response = await this.client.post<UserReadType>(url, { json: data });
		return this.readSchema.parse(response.data);
	}

	async getAll(): Promise<UserReadType[]> {
		const url = this.buildUrl(`${this.pathPrefix}/all`);
		const response = await this.client.get<UserReadType[]>(url);
		return response.data.map((user: UserReadType) => this.readSchema.parse(user));
	}

	async getList({
		searchTerm = null,
		activeOnly = null
	}: {
		searchTerm: string | null;
		activeOnly: boolean | null;
	}): Promise<UserReadType[]> {
		const url = this.buildUrl(`${this.pathPrefix}/list`, { searchTerm, activeOnly });
		const response = await this.client.get<UserReadType[]>(url);
		return response.data.map((user: unknown) => this.readSchema.parse(user));
	}
}
