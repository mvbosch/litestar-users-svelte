import { z } from 'zod';

const userBase = z.object({
  name: z.string(),
  email: z.string().email(),
  createdAt: z.date(),
  updatedAt: z.date(),
});

export const userWriteSchema = userBase.extend({
  password: z.string().min(8),
});
export type UserWriteType = z.infer<typeof userWriteSchema>;

export const userReadSchema = userBase.merge(
  z.object({ id: z.string().uuid() })
);
export type UserReadType = z.infer<typeof userReadSchema>;

export const authenticationSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})
export type AuthenticationSchemaType = z.infer<typeof authenticationSchema>;
