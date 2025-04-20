import { AxiosError } from 'axios';
import type { SuperValidated } from 'sveltekit-superforms';
import { setError } from 'sveltekit-superforms';
import type { BadRequestBody } from '$services/http/response';


export function parseBadRequest(error: AxiosError) {
	const responseBody = error.response?.data as BadRequestBody;
	const errDescription = responseBody.extra[0];
	return { path: errDescription.key, pathError: errDescription.message };
}

export function handleSubmissionErrors<T>(error: unknown, form: SuperValidated<Record<string, unknown>, T>, errorCodeMap: Record<number, Array<string>>) {
	if (error instanceof AxiosError && error.response) {
		const status = error.response.status;
		if (status === 400) {
			const { path, pathError } = parseBadRequest(error);
			return setError(form, path, pathError);
		} else if (status in errorCodeMap) {
			return setError(form, errorCodeMap[status][0], errorCodeMap[status][1]);
		}
	}
	throw error;
}
