require 'rails_helper'

RSpec.describe NetworkDevice, type: :model do
  let(:network_device) { create(:network_device) }

  it 'cannot have comments' do
    expect(network_device).to be_valid
  end
end
