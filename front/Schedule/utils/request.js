
export default (options) => {
	return new Promise((resolve, reject) => {
		uni.request({
			url: "http://127.0.0.1:7777" + options.url,
			method: options.method || "GET",
			data: options.data || {},
			// header : {
			// 'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
			// },
			success: (res) => {
				resolve(res)
			},
			fail: (err) => {
				uni.showToast({
					title: "接口请求失败"
				})
				reject(err)
			}
		})
	})
}