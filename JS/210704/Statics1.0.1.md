# 추정

 점추정은 모수를 추정함에 있어서 하나의 값을 추정하는 방법이다. 

반면에 구간추정은 구간으로 모수를 추정하는 방법이다.

## 점추정

표본의 정보로부터 모집단의 모수를 하나의 값으로 추정하는 것을 말한다.
$$
\hat{\mu}=\bar x\\\hat{\sigma^2}=s^2=V
$$


## 추정량의 성질

좋은 추정량이 되도록 하기 위해서 갖추어야할 대표적인 성질

1. 일치성

    일반적으로 적은 수의 표본보다 많은 수의 표본으로 추정할수록 그 결과를 신뢰한다. 즉 많은 표본으로 추정할수록 추정량이 참값인 모수에 접근하는 성질을 말한다.

2. 불편성

    표본크기 50인 모집단에서 10번 시도하여 표본평균을 구하면 그 값이 다르게 나올 것이다. 그러나 무한시행에서 표본평균의 기대값이 참값과 같을 때, 이 추정향을 불편추정량이라 한다. 

   * 일치성과 불편성은 다른 개념으로 불편성은 표본크기를 고정시켜 두고서 표본만을 되풀이 하여 여러번 추출한 경우를 말하며, 일치성은 표본수를 점점 증가시키는 경우이다.

3. 유효성(최소분산성)

   모수에 대한 불편 추정량은 여러가지가 존재할 수 있다. 

   이 때에 당연히 참값과의 차이가 작을수록 좋은 추정량이라 할 수 있다.  이것을 유효하다고 한다.

   그리고 불편성과 유효성을 동시에 갖는 가장 좋은 추정량을 최소분산불편추정량이라 한다. 

   

## 구간추정

점추정의 문제점은 구한 모수를 확신할 수 없다는 문제가 있습니다. 샘플 수를 늘리면서 수렴시킬 수는 있으나, 시간과 비용의 제약이 따르기에 점추정만을 이용하여 판정하는데는 문제가 있습니다. 이런 문제점을 인지하고 보완하여 사용하는 것이 구간추정이라 할 수 있습니다.

### 정규분포의 모평균 구간추정(모분산 기지)

 표본평균은 아래의 분포를 따른다.
$$
\bar X\sim N(\mu,\frac{\sigma^2}{n})\\
$$
해당 분포를 표준화 하여 95% 구간을 추정하면
$$
P(Z_{0.975} \leq Z=\frac{\bar X-\mu}{{\sigma/ \sqrt n}} \leq Z_{0.025}) = 0.95
$$
이 되고 이 식을 모수에 관해 변환하면 
$$
P(\bar X -Z_{0.025}*\frac{\sigma}{\sqrt n} \leq \mu \leq \bar X -Z_{0.975}*\frac{\sigma}{\sqrt n}) = 0.95
$$


위와 같이 표현할 수 있고,
$$
\bigg[\bar X -Z_{0.025}*\frac{\sigma}{\sqrt n},\bar X -Z_{0.975}*\frac{\sigma}{\sqrt n}  \bigg]
$$
최종적으로 다음과 같이 나타냅니다.
$$
\bigg[\bar X -Z_{\alpha/2}*\frac{\sigma}{\sqrt n},\bar X +Z_{\alpha/2}*\frac{\sigma}{\sqrt n}  \bigg]
$$

### 정규분포의 모분산 구간추정

$$
E(S^2)=E\Big(\frac{1}{n-1} \sum(X_{i}-\bar X)^2 \Big)\\
=\frac{1}{n-1}E\Big[\sum(X_{i}-\mu)^2 -n(\bar X -\mu)^2 \Big]\\
=\frac{1}{n-1}(n\sigma^2 -n\frac{\sigma^2}{n})\\
=\sigma^2
$$


$$
S^2=\frac{1}{n-1} \sum(X_{i}-\bar X)^2\\
(n-1)S^2=\sum(X_{i}-\bar X)^2\\
\frac{(n-1)S^2}{\sigma^2}=\frac{\sum(X_{i}-\bar X)^2}{\sigma^2}
$$
**https://m.blog.naver.com/gdpresent/221138171777**

자세한 설명은 링크 참조
$$
P\Big( \chi^2_{1-\alpha/2}(n-1) \leq \chi^2_{n-1} \leq \chi^2_{\alpha/2}(n-1) \Big)\\
P\Big( \chi^2_{1-\alpha/2}(n-1) \leq \frac{(n-1)S^2}{\sigma^2} \leq \chi^2_{\alpha/2}(n-1) \Big)\\

P\Big( \frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)} \leq \sigma^2 \leq \frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)} \Big)
$$

### 베르누이분포의 모평균 구간추정

베르누이 분포의 표본 평균은 아래의 분포를 따릅니다.
$$
\bar X \sim N\Big ( p,\frac{p(1-p)}{n} \Big)
$$
이를 표준화하면 아래와 같고
$$
Z=(\bar X-p)/\sqrt\frac{p(1-p)}{n}
$$
95% 신뢰구간을 추정하면
$$
0.95\simeq P\Big( Z_{\alpha/2} \leq (\bar X-p)/\sqrt\frac{p(1-p)}{n} \leq Z_{1-\alpha/2} \Big )\\
= P\Big (\bar X -Z_{\alpha/2}\sqrt\frac{p(1-p)}{n} \leq p \leq \bar X -Z_{\alpha/2}\sqrt\frac{p(1-p)}{n} \Big )
$$
최종적으로 일반화 하면 다음과 같다.
$$
\Big [ \bar X -Z_{\alpha/2}\sqrt\frac{p(1-p)}{n},\bar X +Z_{\alpha/2}\sqrt\frac{p(1-p)}{n}\Big]
$$

### 포아송 분포의 모평균 구간추정

포아송 분포는 평균과 분산이 같습니다.  
$$
X \sim P(\lambda)\\
\bar X \sim N(\lambda,\frac{\lambda}{n})
$$
이를 표준화하면 아래의 식으로 표현이 가능합니다.
$$
0.95\simeq P\Big( Z_{\alpha/2} \leq (\bar X-\lambda)/\sqrt\frac{\lambda}{n} \leq Z_{1-\alpha/2} \Big )\\
$$
이번엔 모수에 대하여 정리하면
$$
P\Big( \bar X-Z_{\alpha/2}\sqrt\frac{\lambda}{n} \leq \lambda \leq \bar X+ Z_{\alpha/2}\sqrt\frac{\lambda}{n} \Big )
$$
이제 일반화 시키면 
$$
\Big[ \bar X-Z_{\alpha/2}\sqrt\frac{\lambda}{n},\bar X+ Z_{\alpha/2}\sqrt\frac{\lambda}{n} \Big ]
$$
다음과 같이 정리할 수 있습니다.
