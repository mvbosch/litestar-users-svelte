import { z } from 'zod';

export const configSchema = z.object({
  sessionId: z.string()
})
export type ConfigSchemaType = z.infer<typeof configSchema>;
