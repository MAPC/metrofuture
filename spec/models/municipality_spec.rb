require 'spec_helper'

describe Municipality do

  before { @municipality = Municipality.new(name: "Inner Core") }

  subject { @municipality }
  
  it { should respond_to :geom }
  it { should respond_to :muni_id }
  it { should respond_to :name }
  
  it { should respond_to :community_subtype }
  it { should respond_to :community_type }

  it { should respond_to :subregions }

  it { should be_valid }

  describe "when name is blank" do
    before { @municipality.name = " " }
    it { should_not be_valid }
  end

 describe "when name is too short" do
    before { @municipality.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when name is too long" do
    before { @municipality.name = "a" * 71 }
    it { should_not be_valid }
  end

end
