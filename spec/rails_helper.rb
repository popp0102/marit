require 'spec_helper'

ENV['RAILS_ENV'] ||= 'test'

require_relative '../config/environment'
require 'rspec/rails'

begin
  ActiveRecord::Migration.maintain_test_schema!
rescue ActiveRecord::PendingMigrationError => e
  abort e.to_s.strip
end
RSpec.configure do |config|
  config.include FactoryBot::Syntax::Methods
end

