// neurolnettutorial.cpp

#include <vector>
#include <iostream>

using namespace std;

class Neuron {};

typedef vector<Neuron> Layer;

class Net
{
public:
Net(const vector<unsigned> &topology);
void feedForward(const vector<double> &inputVals);
void backProp(const vector<double> &targetVals);
void getResults(vector<double> &resultVals) const;

private:
vector<Layer> m_layers;// a_Layers layerseum
};

Net::Net(const vector<unsigned> &topology)
{
unsigned numLayers = topology.size();
for (unsigned LayerNum = 0; LayerNum < numLayers; ++LayerNum){
m_layers.push_back(Layer());
// new layer now  fill it neurons
// add a bias neuron to the layer
for (unsigned neuroNum = 0; neuroNum <= topology[LayerNum]; ++neuroNum) {
m_layers.back().push_back(Neuron());
cout << "Made a Neuron!!" << endl;
}
}
}

int main()
{
vector<unsigned> topology;
Net myNet(topology);

vector<double> inputVals;
myNet.feedForward(inputVals);

vector<double> targetVals;
myNet.backProp(targetVals);

vector<double> resultVals;
myNet.getResults(resultVals);

}
