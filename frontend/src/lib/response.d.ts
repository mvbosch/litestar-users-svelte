export type InvalidExtra = {
  message: string;
  key: string;
  source: string;
};
export type BadRequestBody = {
  status_code: number;
  detail: string;
  extra: InvalidExtra[];
}
