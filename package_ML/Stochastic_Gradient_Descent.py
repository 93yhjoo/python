from numpy.random import seed
import numpy as np
class AdalineSGD(object):
    #GD는 단일 반복에서 기울기를 계산하므로 많이 대규모 데이터의 경우 오랜 시간이 걸릴 수 있다.
    #학률적 GD는 데이터를 무작위로 적은 데이터 세트로 중요한 평균값을 추정하는 법이다
    #반복이 충분하다면 효과가 있지만
    # 노이즈가 매우 심하다.
    def __init__(self,eta=0.01, n_iter=10,shuffle=True,random_state=None):
        self.eta=eta
        self.n_iter=n_iter
        self.w_initialized=False
        self.shuffle=shuffle
        if random_state:
            seed(random_state)

    def fit(self,X,y):
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X,y=self._shuffle(X,y)
            cost=[]
            for xi, target in zip(X,y):
                cost.append(self._update_weights(xi,target))
                avg_cost=sum(cost)/len(y)
                self.cost_.append(avg_cost)
                return self

    def partial_fit(self,X,y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
            if y.ravel().shape[0] > 1:
                for xi, target in zip(X,y):
                    self._update_weights(xi,target)
            else:
                self._update_weights(X,y)
            return self

    def _shuffle(self,X,y):
        r=np.random.permutation(len(y))
        return X[r],y[r]

    def _initialize_weights(self,m):
        self.w_=np.zeros(1+m)
        self.w_initialized=True


    def _update_weights(self,xi,target):
        output=self.net_input(xi)
        error=(target-output)
        self.w_[1:]+=self.eta*xi.dot(error)
        self.w_[0] += self.eta * error
        cost=0.5*(error**2)
        return cost

    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]

    def activation(self,X):
        return self.net_input(X)

    def predict(self,X):
        return np.where(self.activation(X) >=  0.0, 1,-1)