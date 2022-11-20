require 'rails_helper'

RSpec.describe NetworkDevicesController, type: :controller do

  context '#index' do
    subject { get :index }

    it 'should not raise error' do
      expect{subject}.to_not raise_error
    end
  end
end

