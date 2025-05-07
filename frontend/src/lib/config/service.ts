import { BaseService } from '$lib/base_service';
import { client } from '$lib/http_client';
import { type ConfigSchemaType, configSchema } from './schema';

export class ConfigService extends BaseService<any, ConfigSchemaType, any> {
  client = client;

  async getConfig(): Promise<ConfigSchemaType> {
    const response = await this.client.get<ConfigSchemaType>(this.buildUrl('/config'));
    return configSchema.parse(response.data);
}}
