https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

> RFC 7231
200 OK
The request has succeeded. The meaning of a success varies depending on the HTTP method:

> 400 Bad Request
This response means that server could not understand the request due to invalid syntax.

> 401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

> 403 Forbidden
The client does not have access rights to the content, i.e. they are unauthorized, so server is rejecting to give proper response. 

> 404 Not Found
The server can not find requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist.

> 408 Request Timeout
This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. 

> 500 Internal Server Error
The server has encountered a situation it doesn't know how to handle.

> 501 Not Implemented
The request method is not supported by the server and cannot be handled.

> 502 Bad Gateway
This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.

> 503 Service Unavailable
The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded.

> 504 Gateway Timeout
This error response is given when the server is acting as a gateway and cannot get a response in time.

> 511 Network Authentication Required
The 511 status code indicates that the client needs to authenticate to gain network access.
