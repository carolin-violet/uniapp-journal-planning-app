<template>
	<view class="article-layout" :style="{backgroundImage:'url('+baseUrl+urlList[Math.floor(Math.random()*urlList.length)]+')'}">
		<view class="article-body">
			<view class="article-head">
				<!-- 标题 -->
				<view class="title">
					{{article.title}}
				</view>
				
				<!-- 作者 -->
				<view class="author">
					{{article.author}}
				</view>
			</view>
			
				
				<!-- 正文内容 -->
				<view class="article-content">
					<text class="paragraph" v-for="(item, index) in article.content">
						{{item}}
					</text>
				</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				article: {},
				article_id: 0,
				baseUrl: '../../static/ACG-detail/',
				urlList: ['0229540187a24035a568982100d44a39.webp', '02770877d3eddb9e616e354088a307f7.webp', '04b2b7a57bd04362b194db316f93e39b.webp', '069471d37213408f85e724f6fb2bee96.webp', '07d2157d2b35b4ad3db9ead7679472f2.webp', '0c600dfaa1cc4360bb83690bd697bf35.webp', '0cbf56d71b9a4c56b1aa72658ef88a48.webp', '12259c58541244688590d802750baca6.webp', '122b271b339e49a3a6105d7a69fa8537.webp', '16989a2a229c4a05aab910392c5f0bbe.webp', '195bbc6d308340f6affa058f98ab74db.webp', '1a84819b802b437bb9251d4dd5559085.webp', '21b1c09746a74a0ca99ece2b738dbc12.webp', '2308c4d43f5848dfa1120b0af1fae6ba.webp', '26ce604178f84bd19b40481a32c5d03e.webp', '36ca76a7eb7c41e4b0bc080ab1eab5a4.webp', '37bd0f7a007f4a68b6b05823d8c0f46d.webp', '3a773d14dd2ebdb21c5bda2926b08be1.webp', '418d82674602483ab9609b6de5b22374.webp', '53f50c66f32a4432b3f3a31dec3a8b20.webp', '56187dfc92a04a93b6d8c55f28510668.webp', '5cfdd6e55d1b415ea23d4310b4764d82.webp', '618e9e5ead0b4cac9b79430ca1912726.webp', '64323d5aaaa6847280b8cf0c86b9b780.webp', '6489ca30db724c6094e3233ac5ac2b2e.webp', '68a5f5a1ef65950b97a6884e95edac8a.webp', '7a1564e33b3c4ade857f75ac6f83a685.webp', '7b87df85ccc54344bf29d85308c61be1.webp', '87833234799d46f59f36b3be2f19b282.webp', '898e94a6dca949019bbaadda62fb8c93.webp', '89f9b551157b4e7e8ba889dd15789446.webp', '8e988bcf17d14e08bc704bfed1f5012a.webp', '8f25ff3207fa9a73751d1cbaf4012d17.webp', '9014b1da20ff48d09e35165c7a9f6b12.webp', '90dc4245ed4f73a273a2e166d831b1dc.webp', '97ed15a308a74c66aef7e7136a59ea72.webp', '982b7107cc3725b3c109e430ee04af8f.webp', '9888248701914d2b9486a56d79185320.webp', '9e7e5b138d294b02bd92c39d9f0f603e.webp', 'a0a6ffb3a3bd4f898b101fad08484df5.webp', 'a0cae7a97d5e47d1b1181609eac767e8.webp', 'a1dd679839a242c88101cc2a25b5bd42.webp', 'a33471ca657249c9857ef7db8b595ed6.webp', 'a365cfbe384947b5ad7396f0aed47a1e.webp', 'a3b067836cc2d410841a423fbbb0a3ae.webp', 'a7db2c996f334832aa2719220da7e2a7.webp', 'a8a45d4a28a44446a20c82d8cb6468ab.webp', 'b1dd495e7b8f45da84d8150520a2015b.webp', 'b3884a89a9301dcdd8ad38763c0690a8.webp', 'b4feb6c45e7341ed8464567982cc6820.webp', 'b96642545d8e444e94c3a8b71bfafb5b.webp', 'bd0b7d17063d432f9664fec1ca959046.webp', 'bddc36f151614e319207792c8898c5f6.webp', 'be0afddb0f4eab14ff0f03df12098920.webp', 'c176c0a4f1be412982a8dc9074c60f50.webp', 'c350655c892f4651a4ef80d15ad4ec83.webp', 'c42a7918884449648faac468c39b4e72.webp', 'c5b516d2c23b47808315e21b740cf527.webp', 'c7451fa644844196bded37a30acf054e.webp', 'c776174b6c83d26667c4d639252ed31e.webp', 'c7f55bce18f9435fb1fc2dc8f85dc510.webp', 'c941de17b7c54316ab76d13df50547ef.webp', 'cc374837746f4019a6c2bb9ac0a3ee93.webp', 'd523eea0fd6142d48b3e94b83a49c6b5.webp', 'd9dc58777bd18d94f534b94bb454e9ff.webp', 'db2eb4b1b9194e6ea7c2219d58c4f960.webp', 'df4a23bfb227f49faf9d7f4923e82a2d.webp', 'e0a4932851d84d7f8bbb2551cec08138.webp', 'e1289dc1a10941ff842c1707e7502b00.webp', 'e1cee15c2720fdf21ddea2b3465f98db.webp', 'e37a32ea5ad34a76863669c48c8aee4c.webp', 'eb3b8660b16f43778467b815ed8b6ccc.webp', 'eeb568eb27e94b6694465c5257b4ce59.webp', 'f34116ff51c14046985d2421853b4419.webp', 'f3d5d6b72e5644ef9c8da226cc33e678.webp', 'f5d08607b33b47dcae9f2149e1965d00.webp', 'f66351b8d99104a262a500c3db262dac.webp', 'f678e49550b2449391323cbf8107b7ac.webp', 'f6e012fbee3940558dfcfa8bd18042c5.webp', 'f8459f6c8ec34c5e93ede21ddfc28a5a.webp', 'fcc97d179fa34e009fd96157c9dccb0b.webp', 'rBAAdmEOhlqADyqZAArVWn1LI_Y359.webp', 'rBAAdmEOhmCAdToXAA-yzznGQwM728.webp', 'rBAAdmEOhmCADWtKAA8icSFdiaA022.webp']
		  }
		},
		methods: {
			async getArticle(article_id) {
				this.article = {}
				this.isCollected = false
				let res = await this.myRequest({
					url: "/articles/" + this.article_id
				})
				this.article = res.data.article
			}
		},
		onLoad(option) {
			this.article_id = option.article_id
			this.getArticle(this.article_id)
		}
	}
</script>

<style lang="less" scoped>
	.article-layout{
		width: 100%;
		height: 100%;
		background-size: cover;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-position: center center;
		.article-body{
			height: 1400rpx;
			overflow: auto;
			background-color: rgba(200, 200, 200, 0.6);
			.article-head{
				padding-top: 40rpx;
				text-align: center;
				.title{
					font-size: 60rpx;
					height: 160rpx;
					line-height: 80rpx;
					word-wrap: break-word;
				}
				.author{
					font-size: 30rpx;
					height: 60rpx;
					line-height: 60rpx;
				}
			}
			.article-content{
				display: flex;
				flex-direction: column;
				padding: 30rpx 20rpx;
				.paragraph{
					font-size: 30rpx;
					text-indent: 60rpx;
				}
			}
		}
	}
</style>
