require 'rails_helper'

RSpec.describe NetworkDevice, type: :model do
  let(:network_device) { create(:network_device) }

  context 'initialization' do
    subject { network_device }
    it { expect(subject).to be_valid }
  end
end
