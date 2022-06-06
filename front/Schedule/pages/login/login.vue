<template>
	<view class="login-layout">
		<view class="login-container">
			<view class="avatar-img">
				<image src="../../static/login-avatar.webp"></image>
			</view>
			<view class="main">
				<input type="text" value="" placeholder="账号" placeholder-style="color: #fff" v-model="account"/>
				<input type="password" value="" placeholder="密码" placeholder-style="color: #fff" v-model="password"/>
				<view class="other-item">
					<text>立即注册</text>
					<text>忘记密码?</text>
				</view>
			</view>
			<button @click="login">登录</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				account: "",
				password: ""
			}
		},
		methods: {
			async login() {
				let data = {
					account: this.account,
					password: this.password
				}
				let res = await this.myRequest({
					url: "/login",
					method: 'POST',
					data
				})
				console.log(res.data)
				if (res.data.msg === "登录成功") {
					uni.setStorage({
						key: "user",
						data: JSON.stringify(res.data.info)
					})
					uni.switchTab({
						url:"../personal/personal"
					})
				} else {
					uni.showToast({
						title: "账号或密码错误",
						icon: 'none'
					})
					this.password = ''
				}
			}
		}
	}
</script>

<style lang="less" scoped>
	.login-layout{
		width: 100%;
		background-image: url(../../static/wallpapers/48540923dd54564e7ae4145709f2a084d0584f8a.webp);
		background-position: center center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: cover;
		color: #fff;
		.login-container{
			width: 100%;
			height: 1400rpx;
			background-color: rgba(100,100,100,0.8);
			padding: 120rpx 0;
			.avatar-img{
				width: 200rpx;
				height: 200rpx;
				margin: 0 auto;
				image{
					width: 100%;
					height: 100%;
					border-radius: 50%;
				}
			}
			.main{
				width: 600rpx;
				height: 360rpx;
				margin: 20rpx auto;
				input{
					width: 100%;
					height: 100rpx;
					border-radius: 60rpx;
					margin: 30rpx 0;
					box-shadow: 0 0 15rpx rgba(100, 225, 225, 0.94);
					text-indent: 30rpx;
				}
				.other-item{
					display: flex;
					text{
						flex: 1;
						margin: 0 40rpx;
					}
					text:nth-child(2) {
						text-align: right;
					}
				}
			}
			button{
				width: 400rpx;
				height: 100rpx;
				line-height: 100rpx;
				font-size: 50rpx;
				border-radius: 60rpx;
				background-color: transparent;
				color: #fff;
				box-shadow: 0 0 15rpx rgba(100, 225, 225, 0.94)
			}
		}
	}
</style>
